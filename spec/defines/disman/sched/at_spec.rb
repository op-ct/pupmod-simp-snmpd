require 'spec_helper'

describe 'snmpd::disman::sched::at' do

  let(:title) {'test_at'}
  let(:params) {{
    :oid   => '1234567890',
    :value => 'test_value'
  }}
  base_facts = {
    :interfaces => 'eth0'
  }
  let(:facts){base_facts}

  it { should compile.with_all_deps }
  it { should contain_class('snmpd') }
  it { should create_concat_fragment('snmpd+disman.test_at.at') }
end
